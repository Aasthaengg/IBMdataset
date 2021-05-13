N = int(input())
s1 = input()
s2 = input()
mod = 1000000007

if N == 1:
    answer = 3
elif N == 2:
    answer = 6
else:
    answer = 6
    for i in range(2, N):
        if s1[i] == s2[i]:
            if s1[i - 1] == s2[i - 1]:
                answer = answer * 2 % mod
            else:
                pass
        else:
            if s1[i - 1] == s2[i - 1]:
                answer = answer * 2 % mod
            elif s1[i - 1] != s1[i]:
                answer = answer * 3 % mod
            else:
                pass

print(answer)