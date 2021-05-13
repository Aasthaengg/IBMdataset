n,*bb = map(int, open(0).read().split())

ans = []

while bb:
    imp = True
    for i,v in zip(range(len(bb),0,-1),bb[::-1]):
#         print(i,v)
        if i==v:
            ans.append(v)
            del bb[i-1]
            imp = False
            break
    if imp:
        ans = [-1]
        break

for a in ans[::-1]:
    print(a)