H,W = map(int,input().split())

w = "#"*(2+W)
h = []*H

for i in range(H):
    a = str("#"+input().strip()+"#")
    h.append(a)

print(w)
for j in h:
    print(j)
print(w)