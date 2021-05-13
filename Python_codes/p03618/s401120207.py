def main():
    from collections import Counter
    a=input()
    ans=(len(a)*(len(a)-1))//2+1
    a=Counter(a)
    for i in a.values():
        ans-=((i-1)*i)//2
    print(ans)
main()