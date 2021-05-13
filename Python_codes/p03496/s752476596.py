import sys
input = sys.stdin.readline

def main():
    N = int(input())
    a = list(map(int, input().split()))

    max_ = a[0]
    max_ind = 0
    min_ = a[0]
    min_ind = 0
    for i in range(len(a)):
        if max_ < a[i]:
            max_ = a[i]
            max_ind = i
        if min_ > a[i]:
            min_ = a[i]
            min_ind = i
    ans = []
    if abs(max_) >= abs(min_):
        all_sei = True
        for i in range(N):
            ans.append((max_ind+1, i+1))
    else:
        all_sei = False
        for i in range(N):
            ans.append((min_ind+1, i+1))
    
    if all_sei:
        for i in range(N-1):
            ans.append((i+1, i+2))
    else:
        for i in range(N-1, 0, -1):
            ans.append((i+1, i))
    
    print(len(ans))
    for i in range(len(ans)):
        s, t = ans[i]
        print(s, t)

    


if __name__ == "__main__":
    main()