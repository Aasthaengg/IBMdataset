import numpy as np


def round_up_mean(posi_int_a, posi_int_b):
    val_mean = np.array([posi_int_a, posi_int_b]).mean()
    val_ceiled = int(np.ceil(val_mean))
    print(val_ceiled)


a, b = [int(i) for i in input().split()]
round_up_mean(a, b)
