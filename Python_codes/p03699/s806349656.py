
def main():
    n=int(input())
    s=[int(input()) for _ in range(n)]
    sd=0
    a=sum(s)
    mask=1<<a
    for x in s:
        sd=(sd+1)<<x | sd
    for i in range(a):
        if (a-i)%10!=0 and (mask>>i)&sd>0:
           return print(a-i)
    return print(0)

main()
