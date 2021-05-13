A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word=input()
for i in range(26):
  if A[i]==word:
    print(A[i+1])