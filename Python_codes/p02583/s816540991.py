n = int(input())
l = [int(x) for x in input().split()]
s = [0, 0, 0]
count=0

l.sort()

for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            if i == j or j == k or k==i:
                pass
            else:
                if l[i] >= l[j] or l[j] >= l[k] or l[k] <= l[i]:
                    pass
                else:
                    s[0] = l[i]
                    s[1] = l[j]
                    s[2] = l[k]
                  
                    if s[2] < s[1] + s[0]:
                        count += 1
                    else:
                        pass

print(count)