S = input()

yyyy = int(S[:4])
mmdd = int(S[5:7] + S[8:])

ans = "TBD"

if  yyyy < 2019:
    ans = "Heisei"
elif yyyy == 2019:
    if mmdd <= 430:
        ans = "Heisei"
        
print(ans)