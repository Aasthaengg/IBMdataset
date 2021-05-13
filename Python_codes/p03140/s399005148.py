import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1

def main():
    n=int(input())
    a=input()
    b=input()
    c=input()
    ans=0
    for i in range(n):
        if a[i]==b[i]==c[i]:continue
        elif a[i]==b[i] or b[i]==c[i] or c[i]==a[i]:
            ans+=1
        else:
            ans+=2
    print(ans)

main()