N = int(input());
s = [];
ans = 0;
for i in range(N) :
    s.append(int(input()));
    ans += s[i];

if ans % 10 == 0 :
    s.sort();
    for i in range(N) :
        if s[i] % 10 != 0 :
            ans -= s[i];
            break;
        elif i == N-1 :
            ans = 0;

print(ans);