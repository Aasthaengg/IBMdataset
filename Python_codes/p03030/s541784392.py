import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    res = dict()
    for i in range(n):
        s, n = input().split()
        if s in res:
            res[s].update({int(n): i+1})
        else:
            res[s] = {int(n): i+1}
    for i in sorted(res):
        for j in sorted(res[i].keys(), reverse=True):
            print(res[i][j])
    
if __name__ == '__main__':
    main()