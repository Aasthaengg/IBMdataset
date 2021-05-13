S = input();
str = 'keyence';
ans = 'NO'
if S[:7] == str :
    ans = 'YES';
elif S[-7:] == str :
    ans = 'YES';
else :
    for i in range(1,8) :
        if S[0:i] == str[0:i] and S[-7+i:] == str[-7+i:] :
            ans = 'YES';
            break;

print(ans);
