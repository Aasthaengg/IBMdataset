s=input()
ans=len(s)

while True:
    ans-=2
    s=s[:ans]
    if s[:ans//2]==s[ans//2:]:
        print(ans)
        break