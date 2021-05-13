def actual(N, S):
    number_of_hina_arare_types = len(set(S))

    color_map = {3: 'Three',
                 4: 'Four'}

    return color_map[number_of_hina_arare_types]

N = int(input())
S = input().split()

print(actual(N, S))