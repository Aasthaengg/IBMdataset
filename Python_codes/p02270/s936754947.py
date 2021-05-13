'''
Search - Allocation
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_D

Algorythm
Referenced #1670532 Solution for ALDS1_4_D: Allocation by Chris_Kobayashi

1. Decide the searching point -> (top of the range + bottom of the range) / 2
2. Check whether it is possible to load all of the luggage to the trugs
    in the weight limit of the searching point
3. If it is possible, then move the top to the searching point
   If it is impossible, then move the bottom to the searching point + 1
4. Continue 1~4 as long as the top is greater than bottom

Range
Serching the maximum loading capacity(MLC) number
 between the maximam weight item num and the total weight num

top: total weight num
.
.
. <- search the num point
.
.
bottom: maximam weight item num

Why?
A1. Why not "bot = sp" but "bot = sp + 1"?
Q1. for example
    top = 5
    bot = 3
    sp = (5 + 3) / 2 = 4
    ...
    bot = sp
    sp = (5 + 4) / 2 = 4
    ...
    bot = sp
    ...for inf

A2. Why the top is total weight and bot is max weight?
Q2. Sure it is ok "top = 99999999, bot = 0".
     But, MLC never pass the total weight
      and the limit never be lower than the max.
       So, it is the most effective range.
'''

# input
n, k = map(int,raw_input().split())
w = []
for i in xrange(n):
    w.append(input())

# initial searching range
top = sum(w) # the top of the searching range
bot = max(w) # the bottom of the searching range

# searching until there is no serching range
while top > bot:
    sp = (top + bot) / 2 # the searching point

    tk = 0 # temp index of the trugs
    weight = 0 # temp total weight of a trug

    # check whether it is possible to load all of the luggage
    #  to the trugs in the weight limit of the searching point
    for tw in w:
        if weight + tw <= sp:
            weight += tw
        else:
            tk += 1
            if tk >= k:
                # when impossible, then raise the bottom
                bot = sp + 1
                break
            weight = tw
    else:
        # when possible, then lowering the top
        top = sp

# output MLC
print top