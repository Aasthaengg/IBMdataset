#!/usr/bin/env python3

S = input()

A = [-1] * (len(S) + 1)

if S[-1] == '>':
    A[len(S)] = 0
if S[0] == '<':
    A[0] = 0
for i in range(len(S) - 1):
    if S[i] == '>' and S[i+1] == '<':
        A[i+1] = 0

for i in range(len(S)):
    if S[i] == '<' and A[i] > A[i+1]:
        A[i+1] = A[i] + 1

for i in reversed(range(len(S))):
    if S[i] == '>' and A[i] <= A[i+1]:
        A[i] = A[i+1] + 1

ans = 0
for a in A:
    ans += a
print(ans)
