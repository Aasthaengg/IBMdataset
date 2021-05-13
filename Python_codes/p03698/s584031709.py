s=input()
res="yes"
for i in range(97,123):
    if s.count(chr(i))>1:
        res="no"
        break
print(res)