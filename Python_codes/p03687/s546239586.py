s = input()
def f(s,c):
    result = 0
    while len(set(s)) != 1:
        t = ""
        for i in range(len(s)-1):
            #print(s)
            if s[i] == c or s[i+1] == c:
                #print(s[i],s[i+1],c)
                t += c
            else:
                t += s[i]
        #print(t)
        s = t
        result += 1
    return result
result = float('inf')
for c in set(s):
    result = min(result, f(s,c))
print(result)
