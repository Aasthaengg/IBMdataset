n = int(input())
s=input()

ans=s.count("R")*s.count("G")*s.count("B")

for start in range(n):
    for kousa in range(n):
        if start+2*kousa>n-1:
            break
        if s[start]!=s[start+kousa] and s[start+kousa]!=s[start+2*kousa] and s[start+2*kousa]!=s[start]:
            ans-=1

print(ans)