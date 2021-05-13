h,w=map(int,input().split())
he=""
for i in range(w+2):
    he=he+"#"
print(he)
for i in range(h):
    print("#"+input()+"#")
print(he)