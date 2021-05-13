def carriable_baggage(baggage, baggage_num, truck_capacity, truck_num):
    """Return the number of baggae which trucks can carry."""
    laden_baggage = 0
    for i in range(truck_num):
        laden_weight = 0
        while laden_weight + baggage[laden_baggage] <= truck_capacity:
            laden_weight += baggage[laden_baggage]
            laden_baggage += 1
            if laden_baggage == baggage_num:
                return baggage_num
    return laden_baggage

def min_capacity(baggage, baggage_num, truck_num):
    """Return the minimum value of maximum load capacity of trucks."""
    left = 0
    right = 10000 * baggage_num
    while right - left > 1:
        mid = (left + right) // 2
        v = carriable_baggage(baggage, baggage_num, mid, truck_num)
        if v >= baggage_num:
            right = mid;
        else:
            left = mid
    return right


import sys

n, k = map(int, sys.stdin.readline().split())

T = list(map(int, sys.stdin))

P = min_capacity(T, n, k)

print(P)