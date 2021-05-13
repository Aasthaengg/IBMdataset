import sys
from copy import deepcopy as copy

def main():
    input = sys.stdin.readline
    n = int(input())
    a = [None]*n
    for i in range(n):
        a[i] = [int(x)-1 for x in input().split()]
    
    index = [0]*n
    search = [int(x) for x in range(n)]
    ans = 0
    while True:
        already = set()
        judge = True
        sub = []
        for key in search:
            if index[key] == n-1:
                continue
            key2 = a[key][index[key]]
            if index[key2] == n-1:
                continue
            if key != a[key2][index[key2]]:
                continue
            if key in already or key2 in already:
                continue
            already.add(key)
            already.add(key2)
            index[key] += 1
            index[key2] += 1
            sub.append(key)
            sub.append(key2)
            judge = False
        if judge:
            break
        ans += 1
        search = copy(sub)
        
    for value in index:
        if value != n-1:
            print(-1)
            sys.exit()
    print(ans)
    
if __name__ == "__main__":
    main()