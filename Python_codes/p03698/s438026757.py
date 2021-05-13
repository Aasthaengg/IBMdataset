def actual(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return 'no'
    
    return 'yes'

s = input()
print(actual(s))