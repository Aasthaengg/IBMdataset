n = int(input());
ans = 0;
all9 = 1;
while n//10 > 0 :
    ans += 9;
    if all9 == 1 and (n - n//10*10) < 9 :
        all9 = 0;
    n = n//10;

if all9 == 1 :
    ans = ans + n;
else :
    ans = ans + n - 1;

print(ans);
