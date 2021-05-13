ans = "Good"
s = input()
a =s+"e"
for i in range(len(s)):
    if(a[i]==a[i+1]):
        ans="Bad"
        break
print(ans)