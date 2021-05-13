def main():
    n,k = map(int, input().split())
    s = input()
    a = s[k-1].lower()
    b=list(s)
    b[k-1]=a
    s="".join(b)
    print(s)
main()