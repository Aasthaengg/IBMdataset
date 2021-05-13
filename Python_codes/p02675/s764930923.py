n = input()[-1]
pon = ["0", "1", "6", "8"]

if n == "3":
    ans = "bon"
elif n in pon:
    ans = "pon"
else:
    ans = "hon"
    
print(ans)