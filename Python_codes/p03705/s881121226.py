# vinegar that will do it!!!!!!!!!!!
 
 
N,A,B = map(int, input().split())
 
 

 
 
if N < 2:
    if A == B:
        print(1)
    else:
        print(0)
elif A <= B:
    ans = range((A+B) + A*(N-2), (A+B) + B*(N-2) + 1)
    print(len(ans))
else:
    print(0)
 
 
