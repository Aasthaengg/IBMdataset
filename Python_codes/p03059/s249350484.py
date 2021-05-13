a, b, t = map(int, input().split())

the_number_of_times = (t + 0.5) // a
the_number_of_biscuits = int(b * the_number_of_times)

print(the_number_of_biscuits)