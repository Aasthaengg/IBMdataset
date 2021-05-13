from collections import Counter
s = input()
t = input()
csm = Counter(s).most_common()
ctm = Counter(t).most_common()
if len(csm)!=len(ctm):
    print('No')
else:
    for i in range(len(csm)):
        if csm[i][1]!=ctm[i][1]:
            print('No')
            break
        if i==len(csm)-1:
            print('Yes')