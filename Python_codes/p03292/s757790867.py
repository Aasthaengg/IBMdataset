a1, a2, a3 = map(int, input().split())
elem1 = abs(a2 - a1) + abs(a3 - a2) 
elem2 = abs(a3 - a1) + abs(a2 - a3)
elem3 = abs(a1 - a2) + abs(a3 - a1)
elem4 = abs(a3 - a2) + abs(a1 - a3)
elem5 = abs(a1 - a3) + abs(a2 - a1)
elem6 = abs(a2 - a3) + abs(a1 - a2)
lst = [elem1, elem2, elem3, elem4, elem5, elem6]

print(min(lst))