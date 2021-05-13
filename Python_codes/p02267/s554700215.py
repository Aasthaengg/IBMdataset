first_set_count = int(input());
first_set = [int(n) for n in input().split()];
second_set_count = int(input());
second_set = [int(n) for n in input().split()];

def linear_search(first_set, second_set):
    count = 0;
    for n in second_set:
        for m in first_set:
            if n == m:
                count += 1;
                break;
    print(count);

linear_search(first_set, second_set);
