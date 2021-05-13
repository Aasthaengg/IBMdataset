s = input()
K = int(input())
 
sub = []
for l in range(1,6):
  for st in range(0,len(s)+1-l):
    sub.append(s[st:st+l])

sub_set = list(set(sub))
sub_set.sort()
print(sub_set[K-1])