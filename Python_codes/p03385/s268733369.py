S = input()
check =["a","b","c"]
_S = []
result =0
for i in S:
    _S.append(i)

for i in _S:
    if i in check:
        check.remove(i)
        result+=1

if result ==3:
    print("Yes")
else:
    print("No")
