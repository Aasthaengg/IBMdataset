# -*- coding: utf-8 -*-
s = list(input())
n = len(s)-1
trueans = []
for i in range(2**n):
    bag = []
    for j in range(n):
        bag.append(s[j])
        if (i>>j) & 1:
            bag.append("+")
    bag.append(s[-1])
    bag.append("+")
    kai = ""
    ans = []
    if "+" in bag:
        for j in bag:
            if j != "+":
                kai += j
            else:
                ans.append(int(kai))
                kai = ""
    trueans.append(sum(ans))
print(sum(trueans))