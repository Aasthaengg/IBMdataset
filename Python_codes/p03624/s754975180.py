s=input()
res="None"
for i in range(97,123):
    if not chr(i) in s:
        res=chr(i)
        break
print(res)