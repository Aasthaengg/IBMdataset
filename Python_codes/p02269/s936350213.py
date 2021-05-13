n=int(input())
dict = set()
for i in range(n):
    word= input().split()
    if word[0] == 'insert':
        dict.add(word[1])
    if word[0]=='find':
            if word[1] in dict:
             print("yes")
            else:
             print("no")
             
