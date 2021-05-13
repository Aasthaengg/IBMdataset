s = input()
w = int(input())
for i in range((len(s)+w-1)//w):
    print(s[w*i],end="")