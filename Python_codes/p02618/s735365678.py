day = int(input())
costlist = input().split() #int型
costs = []
for cost in costlist:
    costs.append(int(cost))

satisfactions = []

for i in range(day):
    satisfactions.append(input().split())

for i in range(day):
    for j in range(26):
        satisfactions[i][j] = int(satisfactions[i][j])

type_output = []

last_date = [0 for x in range(26)]


for d in range(day):
    outtype = 1
    best_score = -99999999
    for i in range(26):
        tmp_last_date = last_date.copy()
        tmp_last_date[i] = d+1
        plus = satisfactions[d][i]
        minus = 0
        for j in range(26):
            minus += costs[j] * (d+1 - tmp_last_date[j])
        current_score = plus-minus
        if current_score >= best_score:
            best_score = current_score
            outtype = i+1
    last_date[outtype-1] = d+1
    type_output.append(outtype)


#print(type_output)

for i in range(day):
    print(type_output[i])
