word = input()
score = word.split(' ')
scin = [0,0]
scin[0] = int(score[0])
scin[1] = int(float(score[1])*100)

ansf = scin[0] * scin[1]
answer = ansf // 100
print(answer)