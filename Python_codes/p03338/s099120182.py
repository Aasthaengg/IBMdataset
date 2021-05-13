n = int(input())
s = input()
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
            "q","r","s","t","u","v","w","x","y","z"]
ans = 0
for i in range(1,n-1):
    x = s[:i]
    y = s[i:]
    comp = 0
    for j in alphabet:
        if j in x and j in y:
            comp += 1
    if comp > ans:
        ans = comp
print(ans)        