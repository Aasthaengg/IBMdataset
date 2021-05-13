# coding: utf-8
# Here your code !
import sys
import collections
import math
import unittest


def calculate_triangle_area():
    try:
        [side_a, side_b, deg_C] = [float(value) for value in input().rstrip().split()]
    except:
        __input_error()
    
    area        = (1/2) * side_a * side_b * math.sin(deg_C * math.pi / 180)
    perimeter   = side_a + side_b + math.sqrt(side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(deg_C * math.pi / 180))
    height      = side_b * math.sin(deg_C * math.pi / 180)
    
    print(area)
    print(perimeter)
    print(height)

def __input_error():
    print("input error")
    return -1

class __TestValueClass(unittest.TestCase):
    def testEqual(self,func,tuples):
        self.testFunction(self.assertEqual,func,tuples)
    
    def testFunction(self,assertfunc,func,tuples):
        #tuples[index] = ([*arguments of func], compared value)
        for item in tuples:
            try:
                if isinstance(item[0], collections.Iterable):
                    assertfunc(func(*item[0]),item[1])
                else:
                    assertfunc(func(item[0]),item[1])
            except Exception as msg:
                swidth = 15
                print("="*50)
                print("-- Assertion Error in '" + func.__name__ + "' --")
                print("arguments".ljust(swidth)+":",item[0])
                print("compared value".ljust(swidth)+":",item[1])
                print("message".ljust(swidth)+":")
                print(msg)
                sys.exit()
        print(func.__name__,": succeeded")
        
#test
if __name__ == "__main__" :

    calculate_triangle_area()
#    test = __TestValueClass()