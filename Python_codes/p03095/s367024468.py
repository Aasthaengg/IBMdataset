from collections import*;input();i=1
for c in Counter(input()).values():i*=c+1
print(~-i%(10**9+7))