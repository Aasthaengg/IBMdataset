x=input()
mini=1e+5
for i in range(len(x)-2):
    mini=min(mini,abs(753-int(x[i:i+3])))
print(mini)