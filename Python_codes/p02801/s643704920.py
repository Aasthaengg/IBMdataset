C=input()
A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(A)-1):
    if A[i]==C:
        print(A[i+1])
        break