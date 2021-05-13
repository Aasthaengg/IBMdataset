# -*- coding: utf-8 -*-
A, B, C = map(str, input().split())

print(['NO', 'YES'][A[len(A)-1] == B[0] and B[len(B)-1] == C[0]])