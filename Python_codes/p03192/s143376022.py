def count_of_2(N):
    count = 0
    for i in list(N):
        if i == '2':
            count += 1

    return count


print(count_of_2(input()))
