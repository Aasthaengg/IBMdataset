def to_b(num):
    ans = "";
    while (num > 0):
        if (num % 2 == 0):
            ans += '0';
        else:
            ans += '1';
        num //= 2;
    return ans[::-1];


def check(s, t):
    for i in range(len(s)):
        if (s[len(s) - i - 1] == t[i] and t[i] == '1'):
            return False;
    return True;


n = int(input());

v = list(map(int, input().split()))
a = [""] * n;
for i in range(n):
    num = v[i];
    a[i] = to_b(num);

tmp = ['0'] * 100
l = 0;
r = 0;
ans = 0;
while (r < n):
    if (check(a[r], tmp)):
        #print(a[r])
        #print(tmp)
        for i in range(len(a[r])):
            if (a[r][len(a[r]) - i - 1] == '1'):
                tmp[i] = '1';
        r += 1;
        ans += r - l;
        #print("!!!!", l, r)
    else:
        for i in range(len(a[l])):
            if (a[l][len(a[l]) - i - 1] == '1'):
                tmp[i] = '0';
        l += 1;
print(ans);
        
