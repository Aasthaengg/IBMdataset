N = int(input())

seeking_range =[0,N-1]
seat_condition = ["" for _ in range(N)]

print(0, flush = True)
seat_condition[0] = input()


if seat_condition[0] != "Vacant":
    for n in range(19):
        next_target = sum(seeking_range)//2
        if seeking_range[0] == N-2:
            next_target = N-1
        print(next_target, flush = True)
        seat_condition[next_target] = input()
        
    
        if "Vacant" in seat_condition:
            break

        if (next_target - seeking_range[0] +1) % 2 == 0:

            if (seat_condition[seeking_range[0]] == seat_condition[next_target]):
                seeking_range[1] = next_target
            else:
                seeking_range[0] = next_target

        else:

            if (seat_condition[seeking_range[0]] == seat_condition[next_target]):
                seeking_range[0] = next_target
            else:
                seeking_range[1] = next_target

  
