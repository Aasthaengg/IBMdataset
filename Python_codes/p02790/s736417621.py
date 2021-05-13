score = list(map(int,input().split()))
score.sort()
word = str(score[0])*score[1]
print(word)