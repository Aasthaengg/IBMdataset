a,b,c,d = int(input()),int(input()),int(input()),int(input())
ans = a if a<=b else b
ans += c if c<=d else d
print(ans)