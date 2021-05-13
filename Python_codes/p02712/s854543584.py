score = int(input())
souwa = int((score*(score+1))/2)
kou3 = score//3
souwa3 = int((kou3*(kou3+1)*3)/2)
kou5 = score//5
souwa5 = int((kou5*(kou5+1)*5)/2)
kou15 = score//15
souwa15 = int((kou15*(kou15+1)*15)/2)
answer = souwa-souwa3-souwa5+souwa15
print(answer)