n = int(input())
total = 0
problems_to_solve = []
for i in range(1,n+1):
    total += i
    problems_to_solve.append(i)
    if total >= n:
        diff =  total - n
        for problem in problems_to_solve:
            if problem != diff:
                print(problem)
        break
    
